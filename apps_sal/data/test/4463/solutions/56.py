(ss, ts) = (sorted(list(input())), list(reversed(sorted(list(input())))))
result = False
min_size = min(len(ss), len(ts))
if ss[:min_size] == ts[:min_size] and len(ss) < len(ts):
    result = True
else:
    for index in range(min(len(ss), len(ts))):
        if ss[index] < ts[index]:
            result = True
            break
if result:
    print('Yes')
else:
    print('No')
