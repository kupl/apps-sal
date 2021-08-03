from collections import Counter
counter = Counter(input())
Bulbasaur = Counter('Bulbasaur')
ans = 0
while (counter & Bulbasaur) == Bulbasaur:
    counter.subtract(Bulbasaur)
    ans += 1
print(ans)
