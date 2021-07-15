def main():
    c, hr, hb, wr, wb = map(int, input().split())
    ans = 0
    for i in range(10**6 + 1):
        if i * wr <= c:
            ans = max(ans, i * hr + ((c - i * wr) // wb) * hb)
        if i * wb <= c:
            ans = max(ans, i * hb + ((c - i * wb) // wr) * hr)
    print(ans)





main()
