time_in_row = [4, 5, 6, 3, 2, 1]

s_in = input()
n = int(s_in[:-1]) - 1
s = ord(s_in[-1]) - ord('a')

k = n // 4
ans = k * 16
ans += time_in_row[s]
if n % 2 == 1:
    ans += 7
print(ans)

