from datetime import datetime, date

dt = datetime(date.today().year, 12, 30, int(input()), 0, 0)
td = abs(dt - datetime(dt.year + 1, 1, 1))
answer = int(td.total_seconds() / (60 * 60))
print(answer)
