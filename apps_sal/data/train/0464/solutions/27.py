class Solution:
    def minOperations(self, n: int) -> int:
        # 평균을 구한다. 평균은 n이 된다.
        # 평균으로 부터 각 거리를 다 더한다.
        # 반으로 나눈다.
        count=0;
        for i in range(n):
            target=(2*i)+1;
            count+=abs(n-target);
        print(count);
        return count//2;

