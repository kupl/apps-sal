#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;
ll experiences[5010];
ll strengths[5010];
ll dp[5010][5010];
int calc( ll x ){
    ll sum = 0;
    while( x ){
        sum += x % 10;
        x /= 10;
    }
    return sum * sum * sum;
}
int main(){
    int N; ll S;
    cin>>N>>S;
    for( int i{1} ; i <= N ; ++i ) cin>>experiences[i];
    strengths[0] = S;
    for( int i{1} ; i <= N ; ++i ) strengths[i] = calc( strengths[i - 1] ) + strengths[i - 1];
    memset(dp, 0, sizeof(dp));
    for( int i{1} ; i <= N ; ++i ) dp[0][i] = (strengths[0] * experiences[i]) + dp[0][i - 1];
    for( int i{1} ; i <= N ; ++i )
        for( int j{i + 1} ; j <= N ; ++j )
            dp[i][j] = max(dp[i - 1][j - 1], (strengths[i] * experiences[j]) + dp[i][j - 1]);
    ll output = 0;
    for( int i{0} ; i <= N ; ++i ) output = max(output, dp[i][N]);
    cout<<output;
    return 0;
}
