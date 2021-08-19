MOD = 10 ** 9 + 7
N = input()
ans = 'Yes' if sum(map(int, N)) % 9 == 0 else 'No'
print(ans)
