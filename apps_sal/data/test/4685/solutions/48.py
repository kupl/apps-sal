num1, num2, num3 = map(int, input().split())
count = int(input())

max_num = max(num1, max(num2, num3))

sum_num = num1 + num2 + num3 - max_num
end_num = max_num
for i in range(count):
    end_num *= 2

print(sum_num + end_num)
