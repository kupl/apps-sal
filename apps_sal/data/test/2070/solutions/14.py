def main():
    from collections import defaultdict
    a = list(map(int, input().split()))
    s = input()
    count = 0
    m = [0]*26
    num = [0]*len(s)
    pos = []
    for i in range(26):
        pos.append(list())
    for i in range(len(s)):
        num[i] += a[ord(s[i])-ord('a')]
        if i:
            num[i] += num[i-1]
        pos[ord(s[i])-ord('a')].append(i)
    #print(pos, num)
    for i in range(26):
        tr = defaultdict(lambda: 0)
        if len(pos[i])> 1:
            for j in range(len(pos[i])):
                count += tr[num[pos[i][j]-1]]
                tr[num[pos[i][j]]] += 1
    print(count)
    #print(a, s)
def __starting_point():
    main()

__starting_point()
