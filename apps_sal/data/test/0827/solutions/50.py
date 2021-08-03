n = int(input())
t = input()

s = "110" * (10 ** 5)

if t == "1":
    print(2 * 10 ** 10)
    return


for i in range(3):
    if t == s[i: i + n]:
        print(1 + (3 * 10 ** 10 - (i + n)) // 3)
        return

print(0)
