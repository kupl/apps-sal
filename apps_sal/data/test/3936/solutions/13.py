n = int(input())
s1 = input()
s2 = input()
mod = 10**9 + 7


def rle(string):
    rle_str = string[0]
    rle_cnt = 1
    ans_l = []
    for i in range(1, len(string)):
        if rle_str == string[i]:
            rle_cnt += 1
        else:
            ans_l.append([rle_str, rle_cnt])
            rle_str = string[i]
            rle_cnt = 1
    ans_l.append([rle_str, rle_cnt])
    return ans_l


rle_s = rle(s1)

if rle_s[0][1] == 1:
    ans = 3
    left = 1
elif rle_s[0][1] == 2:
    ans = 6
    left = 2

for s, i in rle_s[1:]:
    if left == 1 and i == 1:
        ans *= 2
    elif left == 1 and i == 2:
        ans *= 2
    elif left == 2 and i == 1:
        ans *= 1
    elif left == 2 and i == 2:
        ans *= 3
    left = i

print((ans % mod))
