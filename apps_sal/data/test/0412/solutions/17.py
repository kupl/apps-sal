input()
numbers = list(map(int, input().split(' ')))


def max2pow(number):
    answer = []
    for y in range(0, 1000):
        if number % pow(2, y) == 0:
            answer.append(y)
    return max(answer)


ans = []
for x in numbers:
    ans.append(max2pow(x))
ans = pow(2, max(ans))
ans1 = 0
for x in numbers:
    if x % ans == 0:
        ans1 += 1
print(ans, ans1)
