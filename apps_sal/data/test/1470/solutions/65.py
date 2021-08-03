# https://atcoder.jp/contests/arc068/tasks/arc068_a

x = int(input())

ans = (x // 11) * 2
mod = x % 11
if mod == 0:
    pass
elif mod < 7:
    ans += 1
else:
    ans += 2

print(ans)
