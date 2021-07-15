A, B, C = map(int, input().split())
sound_count = B // A
if sound_count >= C:
    answer = C
else:
    answer = sound_count
print(answer)
