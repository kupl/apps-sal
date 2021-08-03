n, seq = int(input()), list(map(int, input().split()))
counter = found = 0
for i in range(n):
    if seq[i] == i:
        counter += 1
    else:
        found += (seq[seq[i]] == i)
print(counter + 2 * (found > 0) + (counter < n and not found))
