def main():
    k = int(input())
    n = [int(i) for i in input()]
    s = sum(n)
    n.sort()
    an = 0
    sm = 0
    if s >= k:
        print(0)
    else:
        while sm < k - s:
            sm += 9 - n[an]
            an += 1
        print(an)

main()
