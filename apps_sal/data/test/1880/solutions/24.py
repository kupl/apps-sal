n = input()
n = int(n[0] + n[2] + n[4] + n[3] + n[1])
ans = n ** 5 % 10 ** 5
ans = (5 - len(str(ans))) * '0' + str(ans)
print(ans)
