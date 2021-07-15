def atc_160b(X: int) -> int:
    return X // 500 * 1000 + X % 500 // 5 * 5


X_input = int(input())
print(atc_160b(X_input))
