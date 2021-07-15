n = int(input())
arr = list(map(int, input().split(" ")))

# Sort arr, firstly
arr.sort(reverse=True)

a_arr = []
b_arr = []

for (i, ele) in enumerate(arr):
    # Alice
    if i % 2 == 0:
        a_arr.append(ele)
    # Bob
    else:
        b_arr.append(ele)

print(sum(a_arr) - sum(b_arr))
