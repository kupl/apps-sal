
N = int(input().strip())
AB_list = [list(map(int, input().rstrip().split())) for i in range(N)]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


fish = {}
cnt_A0_B0 = 0
cnt_A0_Bj = 0
cnt_Ai_B0 = 0
mod = 10**9 + 7


for a, b in AB_list:
    if a == b == 0:
        cnt_A0_B0 += 1

    elif (a == 0):
        cnt_A0_Bj += 1

    elif (b == 0):
        cnt_Ai_B0 += 1

    else:
        g = gcd(abs(a), abs(b))

        a //= g
        b //= g

        if a < 0:
            a *= (-1)
            b *= (-1)

        fish.setdefault((a, b), 0)
        fish[(a, b)] += 1


ans = 1
used = set()

for key_a, key_b in fish:
    if (key_a, key_b) not in used:

        if key_b >= 0:
            key_reverse = (key_b, -key_a)
        else:
            key_reverse = (-key_b, key_a)

        if key_reverse in fish:
            ans *= ((pow(2, fish[(key_a, key_b)], mod) - 1) + (pow(2, fish[key_reverse], mod) - 1) + 1) % mod
            ans %= mod

            used.add(key_reverse)

        else:
            ans *= (pow(2, fish[(key_a, key_b)], mod))
            ans %= mod


ans *= ((2**cnt_A0_Bj - 1) + (2**cnt_Ai_B0 - 1) + 1) % mod
ans %= mod

ans += cnt_A0_B0
ans %= mod

ans -= 1

ans = (ans + mod) % mod
print(ans)
