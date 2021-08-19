#!/usr/bin/env python3

total_episodes = int(input())
watched_episodes = list(map(int, input().split()))
total_sum = total_episodes * (total_episodes + 1) // 2
watched_sum = sum(watched_episodes)
print(total_sum - watched_sum)
