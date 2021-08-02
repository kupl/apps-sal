s = input()
t = input()
res = "No"


def rotate(a):
    n = len(a)
    a = a[n - 1] + a[:n - 1]
    return a


for i in range(len(s)):
    if s == t:
        res = "Yes"
        break
    s = rotate(s)

print(res)
