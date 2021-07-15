def main():

    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    ex = [0]
    for x in p:
        ex.append(ex[-1] + (x+1)/2)

    ans = 0
    for i in range(k, n+1):
        ans = max(ans, ex[i] - ex[i-k])

    print(ans)

main()
