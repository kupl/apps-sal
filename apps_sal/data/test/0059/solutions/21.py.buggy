
n = int(input())
raw_input = list(map(int, input().split()))
raw_string = input()

supposed_sum = 0
actual_sum = 0

for i in range(1, len(raw_string) + 1):
    supposed_sum += i
    actual_sum += raw_input[i - 1]
    if raw_string[i - 1] == '0':
        #        print(i, actual_sum, supposed_sum)
        if actual_sum != supposed_sum:
            print("NO")
            return
        actual_sum = 0
        supposed_sum = 0

print("YES")
