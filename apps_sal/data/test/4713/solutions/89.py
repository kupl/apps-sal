(N, S) = (int(input()), input())
print(max([(t := S[:m + 1]).count('I') - t.count('D') for m in range(N)] + [0]))
