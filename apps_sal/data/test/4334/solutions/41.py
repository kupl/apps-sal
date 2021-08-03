S, T = input().split()
A, B = map(int, input().split())
ans = {S: A, T: B}
ans[input()] -= 1
print(*ans.values())
