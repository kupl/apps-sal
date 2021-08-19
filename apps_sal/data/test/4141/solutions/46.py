N = int(input())
A = list(map(int, input().split()))
review_result = 'APPROVED'
for i in A:
    if i % 2 == 0:
        if i % 3 != 0 and i % 5 != 0:
            review_result = 'DENIED'
            break
        else:
            review_result = 'APPROVED'
print(review_result)
