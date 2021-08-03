from heapq import heappush, heappop

h = []
ans = []


def main():
    nonlocal h

    n = int(input())
    for i in range(n):
        s = input()
        if s[0] == 'i':
            data = int(s.split()[1])
            heappush(h, data)
            ans.append(s)
        elif s[0] == 'g':
            data = int(s.split()[1])
            while h and h[0] < data:
                heappop(h)
                ans.append('removeMin')
            if (not h) or (h[0] > data):
                heappush(h, data)
                ans.append('insert ' + str(data))
            ans.append(s)
        else:
            if not h:
                ans.append('insert 0')
            else:
                heappop(h)
            ans.append('removeMin')

    print(len(ans))
    print("\n".join(ans))


def __starting_point():
    main()


__starting_point()
