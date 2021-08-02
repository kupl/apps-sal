import heapq
n = int(input()); m = n; ans, hp_dgt = [], []
for i in range(n):
    s = input(); a = s.split()
    if a[0] == 'insert':
        heapq.heappush(hp_dgt, int(a[1]))
    elif a[0] == 'removeMin':
        if hp_dgt:
            heapq.heappop(hp_dgt)
        else:
            m += 1; ans.append('insert 1')
    elif a[0] == 'getMin':
        x = int(a[1])
        while hp_dgt:
            if hp_dgt[0] < x:
                m += 1; ans.append('removeMin'); heapq.heappop(hp_dgt)
            else:
                break
        else:
            m += 1; ans.append('insert ' + str(x)); heapq.heappush(hp_dgt, x)
        if hp_dgt[0] > x:
            m += 1; ans.append('insert ' + str(x)); heapq.heappush(hp_dgt, x)
    ans.append(s)
print(m)
print('\n'.join(ans))
