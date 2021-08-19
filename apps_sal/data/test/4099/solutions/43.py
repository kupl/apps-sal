(sub_num, full_score, average) = map(int, input().split())
scores = list(map(int, input().split()))
required_score = average * sub_num - sum(scores)
if full_score >= required_score:
    if required_score <= 0:
        print(0)
    else:
        print(required_score)
else:
    print(-1)
