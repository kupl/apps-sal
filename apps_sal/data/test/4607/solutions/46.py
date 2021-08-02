month, day = map(int, input().split())
takahashi_days = month
if day >= month:
    print(takahashi_days)
elif month > day:
    print(takahashi_days - 1)
