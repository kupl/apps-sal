A, B, C = map(int,input().split())
def answer():
    for i in range(1, B+1):
        if A * i % B == C:
            return ("YES")
    return ("NO")

print(answer())
