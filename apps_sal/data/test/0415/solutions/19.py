"""

created by shuangquan.huang at 11/20/18


We get more and more news about DDoS-attacks of popular websites.

Arseny is an admin and he thinks that a website is under a DDoS-attack if the total number of requests for a some
period of time exceeds 100⋅𝑡, where 𝑡 — the number of seconds in this time segment.

Arseny knows statistics on the number of requests per second since the server is booted.
He knows the sequence 𝑟1,𝑟2,…,𝑟𝑛, where 𝑟𝑖 — the number of requests in the 𝑖-th second after boot.

Determine the length of the longest continuous period of time, which Arseny considers to be a DDoS-attack.
A seeking time period should not go beyond the boundaries of the segment [1,𝑛].

Input
The first line contains 𝑛 (1≤𝑛≤5000) — number of seconds since server has been booted.
The second line contains sequence of integers 𝑟1,𝑟2,…,𝑟𝑛 (0≤𝑟𝑖≤5000), 𝑟𝑖 — number of requests in the 𝑖-th second.

Output
Print the only integer number — the length of the longest time period which is considered to be a DDoS-attack by Arseny.
If it doesn't exist print 0.

"""
N = int(input())
A = [int(x) for x in input().split()]
ans = 0
left = [0] * (N + 1)
for i in range(1, N + 1):
    left[i] = left[i - 1] + A[i - 1]
for l in range(N):
    for r in range(l + 1, N + 1):
        count = left[r] - left[l]
        if count > 100 * (r - l):
            ans = max(ans, r - l)
print(ans)
