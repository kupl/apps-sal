  
def atc_165b(X: int) -> int:
    savings = 100
    years = 0

    while savings < X:
        years += 1
        # savings += savings * 0.01 * 100 // 100
        savings += savings // 100
    return years


X = int(input())
print((atc_165b(X)))

