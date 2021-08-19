def main():
    l = list(map(int, input().split()))
    (even, odd) = ([], [])
    for i in l:
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    even.sort()
    odd.sort()
    if len(even) == 3:
        return (even[2] * 2 - even[0] - even[1]) // 2
    if len(even) == 2:
        a = max(odd[0], even[1] + 1)
        b = min(odd[0], even[1] + 1)
        return (a * 2 - (even[0] + 1) - b) // 2 + 1
    if len(odd) == 2:
        a = max(even[0], odd[1] + 1)
        b = min(even[0], odd[1] + 1)
        return (a * 2 - (odd[0] + 1) - b) // 2 + 1
    if len(even) == 0:
        return (odd[2] * 2 - odd[0] - odd[1]) // 2


ans = main()
print(ans)
