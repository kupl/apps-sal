n = int(input())

for i in range(n):
    answer = 0
    d = set()
    m = int(input())
    arr = [int(x) for x in input().split()]
    for j in arr:
        if j % 2 == 0:
            if j not in d:
                d.add(j)
    s = list(d)
    s.sort(reverse=True)

    for j in s:
        ch = j // 2
        answer += 1
        while ch % 2 == 0:
            if ch not in d:
                ch //= 2
                answer += 1
            else:
                break
    
    print(answer)
