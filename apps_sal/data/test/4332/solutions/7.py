
N = int(input())
S_N = sum(list(map(int, list(str(N)))))
ans = N % S_N
print("Yes") if ans == 0 else print("No")
