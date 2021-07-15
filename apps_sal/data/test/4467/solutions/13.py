def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()
    
    n = int(input())
    red = [tuple(map(int, input().split())) for _ in range(n)]
    blue = [tuple(map(int, input().split())) for _ in range(n)]

    red.sort()
    blue.sort()

    now = 0
    for i in blue:
        while now < len(red) and red[now] < i:
            now += 1
        
        l = red[:now]
        if l == []:
            continue

        l = sorted(l, key=lambda x: x[1])
        if l[0][1] > i[1]:
            continue
        
        # binary search
        left = 0
        right = len(l) - 1
        while left < right:
            center = (left + right + 1) // 2
            if l[center][1] < i[1]:
                left = center
            else:
                right = center - 1

        red.remove(l[left])
        now -= 1

    print(n - len(red))

main()
