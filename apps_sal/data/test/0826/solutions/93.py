# k = 1からnまでの k の和
def sigma1(n):
    return n * (n + 1) // 2

n = int(input())

def do():
    l = 0
    h = n
    while l <= h:
        mid = (l + h) // 2
        if sigma1(mid) <= (n + 1):  # 買うことができるなら
            l = mid + 1  # 買えるのでそれ以上の数
        else:  # 買えないなら
            h = mid - 1  # 買えないのでそれ以下の数をトライ
    return (h if (sigma1(h) <= (n + 1)) else l)

x = do()
#print(x)
print(1 + (n - do()))
