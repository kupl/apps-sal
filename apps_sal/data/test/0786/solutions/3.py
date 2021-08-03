num_contests = int(input())

rating = 0

upper_bound = None
lower_bound = None

for contest_num in range(num_contests):
    ci, di = list(map(int, input().split()))

    if di == 1:
        if upper_bound is None or rating < upper_bound:
            upper_bound = rating
    else:
        assert di == 2
        if lower_bound is None or rating > lower_bound:
            lower_bound = rating

    rating += ci

if lower_bound is None:
    print("Infinity")
elif upper_bound is not None and lower_bound >= upper_bound:
    print("Impossible")
else:
    print(rating - (lower_bound + 1) + 1900)
