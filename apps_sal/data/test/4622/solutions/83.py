N = int(input())
A = input().split()
ans = 'YES' if len(A) - len(set(A)) == 0 else 'NO'
print(ans)
