males = int(input())
males_ability = [int(m) for m in input().split()]
females = int(input())
females_ability = [int(m) for m in input().split()]
males_ability.sort()
females_ability.sort()
pairs = 0
for x in males_ability:
    for y in females_ability:
        if y in range(x-1, x+2):
            females_ability.remove(y)
            pairs += 1
            break
print(pairs)



