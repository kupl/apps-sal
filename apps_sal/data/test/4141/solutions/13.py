cnt = int(input())
num_list = [num for num in map(int, input().split()) if num % 2 == 0]

for _ in num_list:
    if _ % 3 == 0 or _ % 5 == 0:
        continue
    else:
        print("DENIED")
        break
else:
    print("APPROVED")

