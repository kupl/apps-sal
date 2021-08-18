

base = 27


def getnum(x):
    return ord(x) - ord("a") + 1


m30 = (1 << 30) - 1
m31 = (1 << 31) - 1
m61 = (1 << 61) - 1
mod = m61
positive_delta = m61 ** 4


def mul(a, b):
    au = a >> 31
    ad = a & m31
    bu = b >> 31
    bd = b & m31
    mid = ad * bu + au * bd
    midu = mid >> 30
    midd = mid & m30
    return calcmod(au * bu * 2 + midu + (midd << 31) + ad * bd)


def calcmod(a):
    au = a >> 61
    ad = a & m61
    res = au + ad
    if res >= m61:
        res -= m61
    return res


def rollinghash(s):
    num = len(s)
    res = [0] * (num + 1)
    pow_base = [1] * (num + 1)
    for i in range(num):
        res[i + 1] = calcmod(mul(res[i], base) + getnum(s[i]))
        pow_base[i + 1] = calcmod(mul(pow_base[i], base))
    return res, pow_base


def search(left, right, rh):
    return calcmod(rh[right] - mul(rh[left], pow_base[right - left]) + positive_delta)


n = int(input())
s = input()
rh, pow_base = rollinghash(s)

ng = n
ok = 0


def hantei(x, rh):
    kumi = {}
    for i in range(n - x + 1):
        temp = search(i, i + x, rh)
        if temp in kumi:
            pre_idx = kumi[temp]
            if i - pre_idx >= x:
                return True
        else:
            kumi[temp] = i
    return False


while ng - ok > 1:
    mid = (ng + ok) // 2
    if hantei(mid, rh):
        ok = mid
    else:
        ng = mid

print(ok)
