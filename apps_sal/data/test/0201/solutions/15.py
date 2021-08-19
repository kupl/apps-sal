import math


def max_joy(max_grams, weight_r, joy_r, weight_b, joy_b, jollies, memoiser):
    if max_grams < 0:
        return 0
    if max_grams == 0:
        return jollies
    if str(max_grams) in memoiser:
        if jollies >= memoiser[str(max_grams)]:
            return 0
    memoiser[str(max_grams)] = jollies
    res1 = max_joy(max_grams - weight_r, weight_r, joy_r, weight_b, joy_b, jollies + joy_r, memoiser)
    res2 = max_joy(max_grams - weight_b, weight_r, joy_r, weight_b, joy_b, jollies + joy_b, memoiser)
    return max(res1, res2)


def main():
    max_grams = 982068341
    weight_r = 55
    joy_r = 57
    weight_b = 106
    joy_b = 109
    memoiser = {}
    jollies = 0
    res = max_joy(max_grams, weight_r, joy_r, weight_b, joy_b, jollies, memoiser)
    print(res)


(c, x, y, a, b) = map(int, input().split())
lim = int(math.sqrt(c))
ans = 0
for i in range(lim):
    if c >= i * a:
        ans = max(ans, x * i + (c - i * a) // b * y)
    if c >= i * b:
        ans = max(ans, y * i + (c - i * b) // a * x)
print(ans)
