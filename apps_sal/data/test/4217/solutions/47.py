n,m = list(map(int, input().split()))
_, *A = list(map(int, input().split()))
food = set(A)
for _ in range(n-1):
    k, *A = list(map(int, input().split()))
    food &= set(A)
print((len(food)))

