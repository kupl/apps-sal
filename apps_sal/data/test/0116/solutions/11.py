3

left1, right1, left2, right2, k = list(map(int, input().split()))

intersection_left = max(left1, left2)
intersection_right = min(right1, right2)

answer = 0
if intersection_right >= k >= intersection_left:
    answer -= 1

if intersection_right >= intersection_left:
    answer += intersection_right - intersection_left + 1

print(answer)

