n = int(input())
s = input()
R = []
G = []
B = []


def f():
    for i in range(n):
        if s[i] == "R":
            R.append(i)
        elif s[i] == "G":
            G.append(i)
        else:
            B.append(i)
    r = len(R)
    g = len(G)
    b = len(B)
    if r == 0 or g == 0 or b == 0:
        return 0
    else:
        ans = r * g * b
        m = 0
        for j in range(1, n - 1):
            for k in range(1, min(j, n - 1 - j) + 1):
                lt = s[j - k]
                md = s[j]
                rt = s[j + k]
                if lt != md and md != rt and rt != lt:
                    m += 1
        return ans - m


print(f())
