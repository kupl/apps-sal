input_X = int(input())

result_500 = input_X // 500
result_500ureshi = result_500 * 1000
result_5ureshi = (input_X - result_500 * 500) // 5 * 5

result = int(result_500ureshi + result_5ureshi)
print(result)
