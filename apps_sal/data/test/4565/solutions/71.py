N = int(input())
r = input()

E_sum = sum(x == "E" for x in r)
W_sum = N - E_sum
left_sum = 0
right_sum = E_sum
min_sum = E_sum
for i in range(N):
    if i == 0:
        if r[i] == "E":
            min_sum -= 1
        prev_sum = min_sum
    else:
        if (r[i - 1], r[i]) == ("W", "W"):
            prev_sum += 1
        elif (r[i - 1], r[i]) == ("E", "W"):
            pass
        elif (r[i - 1], r[i]) == ("E", "E"):
            prev_sum -= 1
        elif (r[i - 1], r[i]) == ("W", "E"):
            pass
    if min_sum > prev_sum:
        min_sum = prev_sum

print(min_sum)
