from collections import Counter
print(sum(x % 2 for x in Counter([int(input())
                                  for _ in range(int(input()))]).values()))
