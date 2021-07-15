length = int(input())
justice = [int(n) for n in input()]
cheater = [int(n) for n in input()]
justice.sort()
cheater.sort()
j_index,cheat_index = 0,0
maximum_ans = 0
while j_index < length and cheat_index < length:
    if justice[j_index] >= cheater[cheat_index]:
        cheat_index += 1
    else:
        j_index += 1
        cheat_index += 1
        maximum_ans += 1

j_index,cheat_index = 0,0
minimum_ans = 0
while j_index < length and cheat_index < length:
    if justice[j_index] <= cheater[cheat_index]:
        cheat_index += 1
        j_index += 1
        minimum_ans += 1
    elif justice[j_index] > cheater[cheat_index]:
        cheat_index += 1

print(length - minimum_ans)
print(maximum_ans)

