n = int(input())
short_ips = []
for i in range(n):
    short_ips.append(input())


# leading zeros can be deleted, but has to have one number remained
# Continuous sequences of 16-bit zero blocks can be shortened to "::"


answers = [[] for x in range(n)]
ans_id = -1
for ip in short_ips:
    ans_id += 1
    visited = False
    segments = ip.split(':')
    for segment in segments:
        if len(segment) == 0:
            if visited:
                answers[ans_id].append("0" * 4)
                continue
            visited = True
            missing = 8 - len(segments)
            for i in range(missing + 1):
                answers[ans_id].append("0" * 4)
        elif len(segment) == 4:
            answers[ans_id].append(segment)
        else:
            leading = 4 - len(segment)
            answers[ans_id].append("0" * leading + segment)

for restored in answers:
    print(':'.join(restored))
